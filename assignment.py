import math


def calculate_skippable_classes():
    # Get user inputs
    total_classes = int(input("Enter total number of classes held so far: "))
    attended_classes = int(
        input("Enter number of classes you have attended: ")
    )

    # Current attendance percentage
    current_percentage = (attended_classes / total_classes) * 100
    print(f"\nYour current attendance is: {current_percentage:.2f}%")

    # Target attendance threshold
    target_percentage = 0.75

    if current_percentage < 75:
        # Calculate how many classes needed to reach 75%
        # (attended + x) / (total + x) >= 0.75  =>  x >= 3*total - 4*attended
        classes_to_attend = math.ceil(3 * total_classes - 4 * attended_classes)
        print(
            f"Your attendance is below 75%. You cannot skip any classes right now."
        )
        print(
            f"You need to attend at least {classes_to_attend} more consecutive class(es) to reach 75%."
        )
    else:
        # Calculate maximum classes you can skip
        # attended / (total + x) >= 0.75  =>  x <= (attended / 0.75) - total
        max_skips = math.floor((attended_classes / target_percentage) - total_classes)
        print(f"You can safely skip up to {max_skips} class(es) without dropping below 75%.")


if __name__ == "__main__":
    calculate_skippable_classes()