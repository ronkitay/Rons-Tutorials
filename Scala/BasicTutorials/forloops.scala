
def main(args: Array[String]) {

  def sequence[A](list: List[Option[A]]): Option[List[A]] = {
    list.foldLeft(Option(List[A]())) {
      (acc: Option[List[A]], value: Option[A]) =>
        if (value.isDefined)
          Option(value.get +: acc.get)
        else
          None[List[A]]
    }
  }

  val allHaveValue = sequence(List(Some("R"), Some("O"), Some("N")))

}

