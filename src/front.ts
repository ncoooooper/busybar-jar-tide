import type {Page} from "@shared/instrument";
import {rect, type Frame} from "@shared/surface";

export function marks(page: Page): Frame {
  if (page.caption !== "JAR TIDE" || page.fraction === undefined) return [];
  const rim = "#ACCBC1FF";
  const jar: Frame = [rect("lip",56,1,12,2,rim),rect("left",55,4,1,10,rim),
    rect("right",68,4,1,10,rim),rect("bottom",56,14,12,1,rim)];
  const height = Math.round(10 * Math.max(0,Math.min(1,page.fraction)));
  if (height) jar.push(rect("balance",57,14-height,10,height,"#6CCFADFF"));
  return jar;
}
