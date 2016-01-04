val nums = List(1,2,3,2,6,1,4,2)

val dups: List[Int] = nums.foldLeft[(Set[Int], Set[Int])]((Set.empty, Set.empty)){
  (acc, value) =>
    val (exists, result) = acc

    if (exists(value))
      (exists, result + value)
    else
      (exists + value, result)
}._2.toList


val dups2: List[Int] =
  nums.groupBy(identity).filter(_._2.size > 1).keySet.toList
