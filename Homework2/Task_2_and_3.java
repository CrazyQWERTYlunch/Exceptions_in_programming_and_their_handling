public class Task_2_and_3 {
    public static void main(String[] args) {
        correctCode2();
        correctCode3();
    }

    private static void correctCode2() {
        try {
            int[] intArray = { 2, 3, 4, 5, 6, 7 };
            int d = 0;
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e);
        }

     private static void correctCode3() throws Exception {
     try {
         int a = 90;
         int b = 3;
         System.out.println(a / b);
         printSum(23, 234);
         int[] abc = {1, 2};
         abc[3] = 9;
    }
    catch (NullPointerException ex) {System.out.println("Указатель не может указывать на null!");
    } catch (IndexOutOfBoundsException ex) {System.out.println("Массив выходит за пределы своего размера!");
    } catch (Throwable ex) {System.out.println("Что-то пошло не так...");
    }
  }

  public static void printSum(Integer a, Integer b) {
    System.out.println(a + b);
  }