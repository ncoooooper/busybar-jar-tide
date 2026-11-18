import {marks} from "./front";
import {instrument} from "@shared/instrument";

instrument({
  marks,
  "title": "JAR TIDE",
  "primary": "Jar Tide",
  "accent": "#71D4C0",
  "cadence": 65000,
  "motion": {enabled:false},
  "setup": "Start companion/serve.py"
});
