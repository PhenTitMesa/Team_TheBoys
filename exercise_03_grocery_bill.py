def exercise_3():
    print("\n" + "=" * 50)
    print("EXERCISE 3: The Grocery Bill")
    print("=" * 50)

    apples = 5
    price_per_apple = 1.50

    total_cost = apples * price_per_apple

    print(f"Number of apples: {apples}")
    print(f"Price per apple: ${price_per_apple:.2f}")
    print("-" * 40)
    print(f"Total cost: ${total_cost:.2f}")

    print("\nOther options:")
    for count in [10, 20, 50]:
        cost = count * price_per_apple
        print(f"  {count} apples = ${cost:.2f}")

    print("=" * 50)
    return total_cost


if __name__ == "__main__":
    result = exercise_3()
    print(f"\nResult: ${result:.2f}\n")
