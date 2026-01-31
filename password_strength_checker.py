import re

def alternating_mix(password):
    """
    Returns the ratio of alternating uppercase/lowercase letters in the password.
    Optimized to use O(1) extra space (no list of letters).
    Ratio = (# of alternating consecutive letter pairs) / (total consecutive pairs)
    Returns ratio (float).
    """
    prev_letter = None  # Store previous alphabet character
    alt_count = 0       # Count of alternating consecutive pairs
    total_pairs = 0     # Total consecutive letter pairs

    for c in password:
        if c.isalpha():
            if prev_letter is not None:
                total_pairs += 1
                # Check if alternating case
                if (prev_letter.isupper() and c.islower()) or \
                   (prev_letter.islower() and c.isupper()):
                    alt_count += 1
            prev_letter = c  # Update previous letter

    if total_pairs == 0:
        return 0  # No consecutive pairs
    return alt_count / total_pairs  # Ratio of alternating pairs

def password_strength(password):
    # Basic criteria
    length_criteria = len(password) >= 8
    lower_criteria = re.search(r"[a-z]", password) is not None
    upper_criteria = re.search(r"[A-Z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    mix_criteria = alternating_mix(password)  # New criterion
    
    # Score calculation
    score = sum([
        length_criteria,
        lower_criteria,
        upper_criteria,
        digit_criteria,
        special_criteria
    ])
    
    # Boost score if alternating mix is strong
    if mix_criteria>0.4 and score >= 4:
        return "Very Strong"
    
    # Normal scoring
    elif score == 5 and mix_criteria>0.2:
        return "A bit Strong"
    elif score == 4 and mix_criteria>0.2:
        return "Strong"
    elif score == 4 and mix_criteria<=0.2:
        return "Moderate"
    elif score == 3:
        return "Weak"
    else:
        return "Very Weak"
    

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
