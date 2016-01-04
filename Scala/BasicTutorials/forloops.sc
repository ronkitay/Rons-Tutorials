def isTriangle(a: Int, b: Int, c: Int): Boolean = { a * a + b * b == c * c }

def sumIsOfThusand(a: Int, b: Int, c: Int): Boolean = {a + b + c == 1000}

var result = for {
  a <- 1 to 1000
  b <- a + 1 to 1000
  c = 1000 - ( a + b )

  if sumIsOfThusand(a, b ,c) && isTriangle(a, b, c)
} yield a * b * c


var streamingResult = for {
  a <- (1 to 100000).toStream
  b <- a + 1 to 1000
  c = 1000 - ( a + b )

  if sumIsOfThusand(a, b ,c) && isTriangle(a, b, c)
} yield a * b * c

streamingResult.headOption


def sequence[A](list: List[Option[A]]) : Option[List[A]] = {
  list.foldRight[Option[List[A]]](Some(Nil)) {
    (e, acc) =>
      for {
        sa <- acc
        a <- e
      } yield a +: sa
  }
}

val allHaveValue = sequence(List(Some("R"), Some("O"), Some("N")))