package Java;

public class best_time_to_buy_and_sell_stock {
    public static int maxProfit(int[] prices) {
        int max_profit = 0;
        int min_price = prices[0];

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < min_price) {
                min_price = prices[i];
            }

            else if (prices[i] - min_price > max_profit) {
                max_profit = prices[i] - min_price;
            }

        }
        return max_profit;
    }

    public static void main(String[] args) {
        int[] prices = { 7, 1, 5, 3, 6, 4 };
        System.out.println(maxProfit(prices));
    }
}
