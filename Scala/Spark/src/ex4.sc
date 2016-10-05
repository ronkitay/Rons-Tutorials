import org.apache.spark.SparkContext
import org.apache.spark.rdd.RDD
import org.apache.spark.rdd.PairRDDFunctions

case class Transaction(from: String, to:String, amount: Long)

case class Scoring(name: String, score: Long)

implicit object TransactionOrdering extends Ordering[(String, Long)] {
  def compare(x: (String, Long), y: (String, Long)): Int = { (x._2 - y._2).toInt }
}

def doit(sc: SparkContext) = {
  val scoringLines = sc.textFile("/Users/rkitay/utils/spark-notebook-0.6.2-scala-2.11.7-spark-1.6.0-hadoop-2.7.1/test_data/scoring.txt")
  val scoring = scoringLines.map {
    line =>
      val splitResult = line.split(""",""")
      Scoring(splitResult(0), splitResult(1).toLong)
  }

  val lines = sc.textFile("/Users/rkitay/utils/spark-notebook-0.6.2-scala-2.11.7-spark-1.6.0-hadoop-2.7.1/test_data/tx.txt")
  val transactions = lines.map {
    line =>
      val splitResult = line.split(""",""")
      Transaction(splitResult(0), splitResult(1), splitResult(2).toLong)
  }

  val scoringRdd = scoring.groupBy(scoring => scoring.name)
  val scoredTransactions = transactions
    .groupBy(transaction => transaction.from)
    .join(scoringRdd)
    .mapValues {
      case (transactions,scorings) => transactions.map(transaction => transaction.amount * scorings.head.score)
    }

  val scoredSums = scoredTransactions.map {
    case (x,y) => (x, y.sum)
//    case (x,y) => (x, y.foldLeft(0l)((agg, elem) => agg + elem))
  }

//  val cachedTransactions = transactions.cache()

//  val froms = cachedTransactions.groupBy(transaction => transaction.from).mapValues(_.map(_.amount).sum)
//  val tos = cachedTransactions.groupBy(transaction => transaction.to).mapValues(_.foldLeft[Long](0)((aggAmount, tx) => aggAmount + tx.amount))
//
//  val maxFrom = froms.max()
//  val maxTo = tos.max()
//
//  val fromFromMaxToToMax = transactions.filter(tx => tx.from == maxFrom._1 && tx.to == maxTo._1).map(_.amount).sum
}

