/**
 * @author Ron Kitay
 * @since 04/01/16
 */

//implicit class RealEquals [TYPE_OF_THIS, TYPE_OF_THAT >: TYPE_OF_THIS] (someType: TYPE_OF_THIS) {
//  def === (otherValue : TYPE_OF_THAT) = someType == otherValue
//}
object Stuff {

  @specialized
  implicit class RealEquals[A](val someValue: A) extends AnyVal {
    def ===(otherValue: A) = someValue == otherValue
  }

}

object MyMain {
  import Stuff._

  val i1 = 1
  val i2 = 2
  val i3 = 1
  val s1 = "1"

  i1 === i2
  i1 === i3
//  i1 === s1
}
