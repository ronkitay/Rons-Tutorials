fun birthdayGreeting(name: String, age: Int): String {
    val nameGreeting = "Happy Birthday, $name!"
    val ageGreeting = "You are now $age years old!"
    return "$nameGreeting\n$ageGreeting"
}

println(birthdayGreeting(name = "Rex", age = 14))
println(birthdayGreeting(age = 4, name = "Lassy"))
