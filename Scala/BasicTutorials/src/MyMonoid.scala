/**
 * @author Ron Kitay
 * @since 04/01/16
 */
abstract class MyMonoid[A] {

  def append(a1: A, a2: A): A

  def zero: A

  object Laws {

    import Equal.EqualOps

    def appendZeroOnRight(a: A)(implicit ea: Equal[A]) = append(a, zero) === a

    def appendZeroOnLeft(a: A)(implicit ea: Equal[A]) = append(zero, a) === a

    def associativeAppend(a1: A, a2: A, a3: A)(implicit ea: Equal[A]) = append(a1, append(a2, a3)) === append(append(a1, a2), a3)
  }

  object MyMonoid {

    implicit object IntMonoid extends MyMonoid[Int] {
      override def append(a1: Int, a2: Int): Int = a1 + a2

      override val zero: Int = 0 // Same as with def
    }

    implicit object StringMonoid extends MyMonoid[String] {
      override def append(a1: String, a2: String): String = a1 + a2

      override def zero: String = ""
    }

    implicit object BooleanMonoid extends MyMonoid[Boolean] {
      override def append(a1: Boolean, a2: Boolean): Boolean = a1 || a2

      override def zero: Boolean = false
    }
  }

}

abstract class Equal[A] {
  def equal(a1: A, a2: A) : Boolean
  object Laws {
    def reflx(a: A) = equal(a,a)
    def symm(a1: A, a2: A) = equal(a1,a2) == equal(a2,a1)
  }

}
object Equal {

  implicit class EqualOps[A](val a1: A) extends AnyVal {
    def ===(a2: A)(implicit ea: Equal[A]) = ea.equal(a1,a2)
  }

  implicit object IntEqual extends Equal[Int]{
    override def equal(i1: Int, i2: Int) = i1 == i2
  }

  implicit class RichSeq[A](val la: Seq[A]) extends AnyVal {
    def areAllEq(implicit ea: Equal[A]): Boolean =
      la.forall(element =>
        element === la.head)
  }

}
