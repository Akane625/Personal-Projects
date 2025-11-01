fun main() {
    val list = listOf("Kotlin", "Java", "C++", "JavaScript", null, null)
    val map = list
        .filterNotNull()
//      .filter {
//          it.startsWith("J")
//        }
//      .map {
//          it.length
//        }
//      .take(3)
//      .takeLast(3)
        .associate { it to it.length }
//      .forEach {
//          println("${it.value}, ${it.key} ") }
    val language = list.filterNotNull().findLast { it.startsWith("foo") }.orEmpty()
    println(language)
}