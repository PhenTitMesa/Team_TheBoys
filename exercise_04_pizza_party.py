def exercise_4():
    print("\n" + "=" * 50)
    print("EXERCISE 4: Pizza Party")
    print("=" * 50)

    total_slices = 20
    friends = 6

    slices_per_person = total_slices // friends
    leftover_slices = total_slices % friends

    print(f"Total slices: {total_slices}")
    print(f"Number of friends: {friends}")
    print("-" * 40)
    print(f"Each person gets: {slices_per_person} slices")
    print(f"Leftover slices: {leftover_slices}")

    exact = total_slices / friends
    print(f"\nExact division: {exact:.2f} slices per person")

    print("\nDistribution:")
    for i in range(friends):
        print(f"Friend {i + 1}: " + "slice " * slices_per_person)
    if leftover_slices > 0:
        print(f"Leftover: " + "slice " * leftover_slices)

    print("=" * 50)
    return slices_per_person, leftover_slices


if __name__ == "__main__":
    each, leftover = exercise_4()
    print(f"\nResult: Each friend gets {each} slices, {leftover} leftover\n")
