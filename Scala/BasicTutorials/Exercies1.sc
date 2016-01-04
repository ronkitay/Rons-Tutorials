def parseRoman(s: Seq[Char]): Int = s match {
  case Seq('I','V', rest @ _*) => 4 + parseRoman(rest)
  case Seq('I','X', rest @ _*) => 9 + parseRoman(rest)
  case 'X' +: rest => 10 + parseRoman(rest)
  case 'V' +: rest => 5 + parseRoman(rest)
  case 'I' +: rest => 1 + parseRoman(rest)
  case _ => 0
}

parseRoman("XXI")
parseRoman("XXII")
parseRoman("XXIII")
parseRoman("XXIV")
parseRoman("XXV")
parseRoman("XXVI")
parseRoman("XXVII")
parseRoman("XXIX")
parseRoman("XXX")


//def areAllEq[A] (sa: Seq[A]) : Boolean = {
//  case e1 +: e2 +: rest => (e1 == e2) && areAllEq(sa.tail)
//  case _ => true
//}
//
//val abc = areAllEq(Seq("A", "B", "C"))
//
//val aaa = areAllEq(Seq("A", "A", "A"))


//val prefixes = List ("aa", "bb")
//val messages = List("aavdsfjk", "bbdsfsdff", "vvfds")
//
//val res = messages.filterNot(message => prefixes.exists(prefix => message.startsWith(prefix)))
//
//
//class Person(val name : String, var age: Int)
//class CarSale(val brand: String, price: Double)
//
//val sales: Map[CarSale, Person] = Map(
//  new CarSale("Ferrari", 9) -> new Person("aaa", 7),
//  new CarSale("Ferrari", 12) -> new Person("aaa", 9)
//)
//
//val youngest = sales
//    .filterKeys(carSale => carSale.brand == "Ferrari")
//    .values
//    .minBy(person => person.age)
//    .name
//
//
//val nums = List(1,2,3)
//
//val sum = nums.foldLeft(0){
//  (acc, e) => acc + e
//}
//
//
//nums.mkString("[", ",", "]")

//

