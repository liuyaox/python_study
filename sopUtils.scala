


//����������ָ�����ں�N������ڣ��ַ���������'2018-09-12'��
//���ߣ���Ң
import java.text.SimpleDateFormat
import java.util.{Calendar,Date}

val dateFormat: SimpleDateFormat = new SimpleDateFormat("yyyy-MM-dd")
val cal:Calendar = Calendar.getInstance()
def getDayAfterNd(dt: Date, interval: Int): String = {
  cal.setTime(dt)
  cal.add(Calendar.DATE, interval)
  dateFormat.format(cal.getTime())
}

//Ӧ��
val yesterdate: Date = dateFormat.parse(getDayAfterNd(new Date(), -1))
val dayBefore2d  = getDayAfterNd(yesterdate, -2)