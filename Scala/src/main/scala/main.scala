import scala.io.Source
import scala.util.control.Breaks._

object Style {
  val BLACK = "\u001B[30m"
  val RED = "\u001B[31m"
  val GREEN = "\u001B[32m"
  val YELLOW = "\u001B[33m"
  val BLUE = "\u001B[34m"
  val MAGENTA = "\u001B[35m"
  val CYAN = "\u001B[36m"
  val WHITE = "\u001B[37m"
  val UNDERLINE = "\u001B[4m"
  val RESET = "\u001B[0m"
}

object Main {

  def sortPair(pair: (Int, Int)): (Int, Int) = {
    if (pair._1 > pair._2) (pair._2, pair._1)
    else pair
  }

  def readNumbersFromFile(filePath: String): List[Int] = {
    try {
      val source = Source.fromFile(filePath)
      val content = source.getLines().mkString
      source.close()

      // Split the content by commas and convert each item to an integer
      content.split(",").map(_.trim.toInt).toList
    } catch {
      case e: java.io.FileNotFoundException =>
        println(s"Error: The file '$filePath' was not found.")
        sys.exit(1)
      case e: NumberFormatException =>
        println("Error: The file contains non-integer values.")
        sys.exit(1)
    }
  }

  def main(args: Array[String]): Unit = {
    val InputArray = List(4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0)
//    val InputArray = List(4, 11, 12, 01)

    var array = InputArray
    var results: List[(Int, Int)] = List()
    var i = 0
    var run = true

    while (run) {
      val arraySize = array.length
      val element = array(i)

      breakable {
        for (k <- 1 until arraySize) {
          println(s"i=$i, k=$k inspected element = $element and ${array(k)}")
          if (element + array(k) == 12) {
            println(Style.RED + "FOUND sum of 2 elements equal to 12" + Style.RESET)
            println(s"i=$i, k=$k, pair=[$element,${array(k)}]")

            val pair = sortPair((element, array(k)))
            results = results :+ pair

            println(s"Array before modification: $array")
            array = array.patch(k, Nil, 1).patch(i, Nil, 1) // Removes the elements at index k and i
            val arraySizeAfterModification = array.length
            println(s"Array after modification: $array")
            println(s"Array size after modification: $arraySizeAfterModification")

            println(s"Input array: $InputArray")
            println(s"Input array size: ${InputArray.length}")

            break // Exit the inner loop
          }
        }
      }

      println(s"k loop increasing i+1 i=$i, arraySize=${array.length}")
      if (i + 1 >= array.length) {
        println("HAND breaking")
        println(array)
        run = false
      }
      i += 1
    }

    // Let's print the results at the end
    println(Style.GREEN + "\nOUTPUT: Let's print the results" + Style.RESET)
    println(s"Input array= $InputArray")
    println(s"Results array= $results")
    println(s"Leftovers array= $array" + Style.RESET)
  }
}




