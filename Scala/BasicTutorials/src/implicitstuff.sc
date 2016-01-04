import scala.util.Try

implicit class IntStuff(theInt: Int) { //extends AnyVal {

  def bug(string: String) = "bug"

  def too(value: Int) = List.fill(value)(theInt)

  def upper() =  theInt * 100

  def reverse() = Try(theInt.toString.reverse.toInt).toOption

}

7.bug("hello")

(1 too 10).map(x => x.toString)
(1 too 10).map(_.toString)

7.upper()


12345689.reverse()
0.reverse()
(-5934).reverse()


//implicit object MyImplicitInt extends Int = 5
implicit val myThirdInt: Int = 3

def usesImplicitParameters(firstInt: Int, secondInt: Int) (implicit thirdInt: Int) = {
  if (firstInt > thirdInt) secondInt
  else firstInt + secondInt
}

val myResult = usesImplicitParameters(7, 3)

// ------------------------------------------------------------------------

//implicit class RealEquals [TYPE_OF_THIS, TYPE_OF_THAT >: TYPE_OF_THIS] (someType: TYPE_OF_THIS) {
//  def === (otherValue : TYPE_OF_THAT) = someType == otherValue
//}
object Stuff {

  implicit class RealEquals[A](val someType: A) extends AnyVal {
    def ===(otherValue: A) = someType == otherValue
  }

}


import Stuff._

val i1 = 1
val i2 = 2
val i3 = 1
val s1 = "1"

i1 === i2
i1 === i3
//i1 === s1


















