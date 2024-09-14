def extract(soup):
    # Find all links with the class 'story-link'
    links = soup.find_all('a', class_='story-link')
    
    # Initialize an empty list to store the extracted information
    mainList = []
    
    # Loop through each link found
    for link in links:
        # Initialize a temporary list to store details of each story
        miniList = []
        
        # Extract the hyperlink and add it to the temporary list
        weblink = link.get('href')
        miniList.append(weblink)
        
        # Extract the title and add it to the temporary list
        title = link.find('div', class_='clear home-right').find('h2', class_='home-title').text
        miniList.append(title)
        
        # Extract the tags and add them to the temporary list
        tags = link.find('div', class_='clear home-right').find('span', class_='h-tags').text
        miniList.append(tags)
        
        # Extract the description and add it to the temporary list
        desc = link.find('div', class_='clear home-right').find('div', class_='home-desc').text
        miniList.append(desc)
        
        # Try to extract the date, if available, and add it to the temporary list
        try:
            date = link.find('div', class_='clear home-right').find('span', class_='h-datetime').text
            miniList.append(date)
        except AttributeError:
            # If date is not found, add a default message
            date = "Date not found"
            miniList.append(date)
        
        # Add the temporary list to the main list
        mainList.append(miniList)
    
    # Return the main list containing all extracted information
    return mainList
