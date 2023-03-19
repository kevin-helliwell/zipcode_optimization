# What This Does

This program uses facts about zipcodes in the United States to deduce a user's possible state location based on their zipcode if location access is not available/provided.

This is intended as logical scaffolding to optimize what listings to show in the absence of user location access for a [project I work on](https://offroadfunfinder.com).

# Logic

If we know based on the zipcode where the user *cannot be*, that means you can render fewer listings.

![image](https://user-images.githubusercontent.com/39539208/226200787-db5ec6bf-3b0e-40db-b1ec-0d030e8794e1.png)

Image Source: https://en.wikipedia.org/wiki/ZIP_Code

# Scratch Work

This is some of the scratch work I did via ExcaliDraw (awesome tool, highly recommend) when I was working through the idea of implementing this repo.

I wanted to account for edge cases, like if the user is on the near the border of two different zipcode groups. I thought a graph would be perfect for this since it will show all the possible scenarios of bordering zipcode groups based on how connected the nodes are.

![image](https://user-images.githubusercontent.com/39539208/226204220-cbab0333-7226-4a76-94d2-181b3c36e162.png)


