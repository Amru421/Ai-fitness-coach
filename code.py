class AIFitnessCoach:
    def __init__(self, age, weight, goal):
        self.age = age
        self.weight = weight
        self.goal = goal.lower()

    def workout_plan(self):
        if self.goal == "weight loss":
            return [
                "30 mins Running",
                "15 mins Skipping",
                "20 mins HIIT",
                "Plank - 3 sets"
            ]
        elif self.goal == "muscle gain":
            return [
                "Push-ups - 4 sets",
                "Weight Training",
                "Squats - 4 sets",
                "Protein Recovery Workout"
            ]
        elif self.goal == "fitness":
            return [
                "Yoga - 20 mins",
                "Walking - 30 mins",
                "Light Strength Training",
                "Stretching"
            ]
        else:
            return ["Invalid goal"]

    def diet_plan(self):
        if self.goal == "weight loss":
            return [
                "Oats & Fruits",
                "Green Vegetables",
                "Lean Protein",
                "Avoid Sugar & Junk Food"
            ]
        elif self.goal == "muscle gain":
            return [
                "High Protein Diet",
                "Eggs, Chicken, Paneer",
                "Rice & Whole Grains",
                "Protein Shake"
            ]
        elif self.goal == "fitness":
            return [
                "Balanced Diet",
                "Fruits & Vegetables",
                "Proper Hydration",
                "Healthy Snacks"
            ]
        else:
            return ["Invalid goal"]

    def show_plan(self):
        print("\n🏋️ Workout Plan:")
        for w in self.workout_plan():
            print("-", w)

        print("\n🥗 Diet Plan:")
        for d in self.diet_plan():
            print("-", d)


# 🔹 User Input
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
goal = input("Enter your goal (weight loss / muscle gain / fitness): ")

# 🔹 AI Coach
coach = AIFitnessCoach(age, weight, goal)
coach.show_plan()
