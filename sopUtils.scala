


//函数：返回指定日期后N天的日期（字符串，形如'2018-09-12'）
//作者：刘尧
import java.text.SimpleDateFormat
import java.util.{Calendar,Date}

val dateFormat: SimpleDateFormat = new SimpleDateFormat("yyyy-MM-dd")
val cal:Calendar = Calendar.getInstance()
def getDayAfterNd(dt: Date, interval: Int): String = {
  cal.setTime(dt)
  cal.add(Calendar.DATE, interval)
  dateFormat.format(cal.getTime())
}

//应用
val yesterdate: Date = dateFormat.parse(getDayAfterNd(new Date(), -1))
val dayBefore2d  = getDayAfterNd(yesterdate, -2)