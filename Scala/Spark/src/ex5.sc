import org.apache.spark.SparkContext

def doit(sc: SparkContext) = {

  class SimpleCSVHeader(header: Array[String]) extends Serializable {
    val index = header.zipWithIndex.toMap

    def apply(array: Array[String], key: String): String = array(index(key))
  }
  val csv = sc.textFile("/Users/rkitay/utils/spark-notebook-0.6.2-scala-2.11.7-spark-1.6.0-hadoop-2.7.1/test_data/2008.csv.full")
  val dataWithHeader = csv.map(line => line.split(",").map(elem => elem.trim))
  val header = new SimpleCSVHeader(dataWithHeader.take(1)(0))
  val dataRows = dataWithHeader.filter(line => header(line, "Year") != "Year")

  val countPerOrigin = dataRows
    .sample(false, 0.001)
    .groupBy(dataRow => header(dataRow, "Origin"))
    .mapValues(_.size)

  countPerOrigin.collect()


  // Count of flights per origin

  // Origin => farthest destination

//  import org.apache.spark.streaming._
//  val ssc = new StreamingContext(sc, Seconds(5))
//
//  val ds = ssc.textFileStream( "/Users/rkitay/utils/spark-notebook-0.6.2-scala-2.11.7-spark-1.6.0-hadoop-2.7.1/test_data/")
//  val dds = ds.flatMap(line => line.split( """\W+"""))
//  val ddds = dds.transform(rdd => rdd.groupBy(identity).mapValues(_.size))
//  ddds.print()
//  ssc.start()

}