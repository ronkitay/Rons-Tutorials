import org.apache.spark.SparkContext

def doit(sc: SparkContext) = {
  val lines = sc.textFile("/Users/rkitay/utils/spark-notebook-0.6.2-scala-2.11.7-spark-1.6.0-hadoop-2.7.1/test_data/daata")
  val words = lines.flatMap(line => line.split("""\W+"""))
  val groups = words.groupBy(identity)
  val result = groups.map(tuple => (tuple._1, tuple._2.size))

  result.collect()

}