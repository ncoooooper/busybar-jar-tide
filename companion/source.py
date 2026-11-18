"""Read one jar from the owner's personal monobank API without exposing account details."""
import json,os,urllib.request
from serve import page
INTERVAL=65
def fetch_info(o):
    req=urllib.request.Request("https://api.monobank.ua/personal/client-info",headers={"X-Token":os.environ["MONO_TOKEN"]})
    with urllib.request.urlopen(req,timeout=8) as r:return json.load(r)
def selected(payload,selector):
    jars=[j for j in payload["jars"] if j.get("id")==selector or j.get("sendId")==selector]
    if len(jars)!=1:raise ValueError("Choose one existing jar ID or sendId")
    j=jars[0];bal=j["balance"];goal=j.get("goal")
    if type(bal) is not int or (goal is not None and type(goal) is not int):raise ValueError("Expected minor currency units")
    return bal,goal,j.get("currencyCode")
def snapshot(o,m):
    bal,goal,cc=selected(fetch_info(o),o["jar"]);previous=m.get("balance",bal)
    if previous!=bal:m["change"]=bal-previous
    m["balance"]=bal;change=m.get("change",0)
    unit={980:"UAH",840:"USD",978:"EUR",985:"PLN",826:"GBP"}.get(cc,str(cc))
    def amount(c):return f"{c/100:,.2f}".replace(","," ")
    progress=bal/goal if goal and goal>0 else None
    level=f"{progress*100:.0f}%" if progress is not None else "No goal"
    pages=[
      page("JAR TIDE",level,amount(bal)+" "+unit,"Remaining "+amount(max(0,goal-bal)) if goal and goal>0 else "Goal not set",fraction=progress),
      page("BALANCE",amount(bal),unit,"Private selection on host"),
      page("LAST CHANGE",("+" if change>0 else "")+amount(change),unit,"Since bridge start")]

    if goal is not None and goal > 0:
        # Work in minor units so rounding never declares a milestone early.
        for percent in (25, 50, 75, 100):
            target = (goal * percent + 99) // 100
            if bal < target:
                pages.append(page("NEXT MILESTONE", f"{percent}%", "Need " + amount(target - bal) + " " + unit,
                                  "At balance " + amount(target), fraction=bal / target))
                break
        else:
            pages.append(page("MILESTONE", "100%", "Goal reached", "Balance " + amount(bal) + " " + unit, fraction=1))
    return dict(state="Selected jar / " + unit, key=str(bal), alert=bal > previous, pages=pages)
