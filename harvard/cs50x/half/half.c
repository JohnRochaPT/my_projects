// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, int tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    // printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
    printf("$%.2f", half(bill_amount, tax_percent, tip_percent));
}

float half(float bill, float tax, int tip)
{
    /// Your function should use the input parameters, bill, tax, and tip, to calculate the final
    /// amount. However, since these values are percentages, you’ll have to do some work to convert
    /// these to more appropriate formats to use for your calculation.
    ///
    /// The tax should be added to the bill amount before calculating the tip. Finally, you will
    /// return exactly half of the full amount, including the bill amount, the tax and the tip.

    /// Lets get the real amounts.
    float total = 0;
    total = bill + ((bill * tax) / 100.00);
    // printf("Bill before tip = [%f]\n",total);
    total = total + ((total * (float) tip) / 100.00);
    // printf("Bill after tip = [%f]\n",total);
    total = (total / (float) 2.00);

    return total;
}
