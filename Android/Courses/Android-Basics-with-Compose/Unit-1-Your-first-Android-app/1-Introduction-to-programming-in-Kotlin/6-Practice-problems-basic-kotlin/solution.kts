// 2 - Print Messages
println("Use the val keyword when the value doesn't change.") 
println("Use the var keyword when the value can change.")
println("When you define a function, you define the parameters that can be passed to it.")
println("When you call a function, you pass arguments for the parameters.")

// 3 - Fix compiler error
println("New chat message from a friend")

// 4 - String templates
var discountPercentage: Int = 0
var offer: String = ""
val item = "Google Chromecast"
discountPercentage = 20
offer = "Sale - Up to ${discountPercentage}% discount on $item! Hurry up!"

println(offer)

// 5 - String concatenation
val numberOfAdults = 20
val numberOfKids = 30
val total = numberOfAdults + numberOfKids
println("The total party size is: $total")

// 6 - Message formatting
val baseSalary = 5000
val bonusAmount = 1000
val totalSalary = "${baseSalary + bonusAmount}"
println("Congratulations for your bonus! You will receive a total of $totalSalary (additional bonus).")

// 7 - Implement basic math operations

val firstNumber = 10
val secondNumber = 5
val result = firstNumber + secondNumber 

println("$firstNumber + $secondNumber = $result")

val firstNumber2 = 10
val secondNumber2 = 5
val thirdNumber2 = 8

val result2 = add(firstNumber2, secondNumber2)
val anotherResult2 = add(firstNumber2, thirdNumber2)

println("$firstNumber2 + $secondNumber2 = $result2")
println("$firstNumber2 + $thirdNumber2 = $anotherResult2")    

println("$firstNumber2 - $thirdNumber2 = ${subtract(firstNumber2, thirdNumber2)}")    

// 8 - Default paremters

val operatingSystem = "Chrome OS"
val emailId = "sample@gmail.com"

println(displayAlertMessage(operatingSystem, emailId))
println(displayAlertMessage(email = emailId))

// 9 - Pedometer

val steps = 4000
val caloriesBurned = pedometerStepsToCalories(steps);
println("Walking $steps steps burns $caloriesBurned calories") 

// 10 - Compare two numbers

println(doWeHaveProblems(timeSpentToday = 300, timeSpentYesterday = 250))
println(doWeHaveProblems(timeSpentToday = 300, timeSpentYesterday = 300))
println(doWeHaveProblems(timeSpentToday = 200, timeSpentYesterday = 220))

// 11 - Moving duplicate code into a function

printWeather("Ankara", 27, 31, 82)
printWeather("Tokyo", 32, 36, 10)
printWeather("Cape Town", 59, 64, 2)
printWeather("Guatemala City", 50, 55, 7)


fun printWeather(city: String, low: Int, high: Int, rain: Int) {
    println("City: $city")
    println("Low temperature: $low, High temperature: $high")
    println("Chance of rain: $rain%")
    println()
}

fun doWeHaveProblems(timeSpentToday: Int, timeSpentYesterday: Int): Boolean {
    return timeSpentToday > timeSpentYesterday
}


fun pedometerStepsToCalories(numberOfSteps: Int): Double {
    val caloriesBurnedForEachStep = 0.04
    val totalCaloriesBurned = numberOfSteps * caloriesBurnedForEachStep
    return totalCaloriesBurned
}


fun add(num1: Int, num2: Int): Int {
    return num1 + num2
}

fun subtract(num1: Int, num2: Int): Int {
    return num1 - num2
}

fun displayAlertMessage(os: String = "Unknown OS", email: String): String {
    return "There's a new sign-in request on $os for your Google Account $email."
}