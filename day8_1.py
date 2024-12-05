def calculate_love_score(name1 , name2):
    combined_name = name1.lower() + name2.lower()
    
    true_count = 0
    love_count = 0
    
    for letter in 'true':
        true_count += combined_name.count(letter)
        
    for letter in 'love':
        love_count += combined_name.count(letter)
        
    love_score = f"{true_count}{love_count}"
    print(f"Love Score : {love_score}")

    
calculate_love_score("Kanye West", "Kim Kardashian")
