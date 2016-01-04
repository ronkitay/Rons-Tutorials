import scala.annotation.tailrec

def factorial(x: Double) =  {

  @tailrec
  def tailFactorial(n: Double, acc:Double): Double = n match {
    case n: Double if n < 2 => acc
    case n => tailFactorial(n - 1,  acc * n)
  }

  tailFactorial(x, 1)
}

factorial(10)


def parseRoman(r: Seq[Char]): Int = {
  @tailrec
  def tailParseRoman(s: Seq[Char], acc: Int): Int = s match {
    case Seq('I', 'V', rest@_*) => tailParseRoman(rest, acc + 4)
    case Seq('I', 'X', rest@_*) => tailParseRoman(rest, acc + 9)
    case 'X' +: rest => tailParseRoman(rest, acc + 10)
    case 'V' +: rest => tailParseRoman(rest, acc + 5)
    case 'I' +: rest => tailParseRoman(rest, acc + 1)
    case _ => acc
  }

  tailParseRoman(r, 0)
}

parseRoman('I' +: 'V' +: List.fill(1000000)('X'))
parseRoman("IV" + List.fill(1000)('X').mkString)

