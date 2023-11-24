public class PrimeDetect {
    public boolean isPrime (int num) {
        if (num < 2) return false;
        if (num == 2 ) return true;
        if (num % 2 == 0) return false;
        for (int i = 3; i <= (int)Math.sqrt(num); i+=2) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
