window.addEventListener('load', (event) => {
    console.log('page is fully loaded');
});



function getGit() {
    fetch("https://api.github.com/users/adion81")
    .then(response => response.json() )
    .then(coderData => {
        console.log(coderData);

        // display name
        let nameTag = document.querySelector("#name");
        let coderName = coderData['name'];
        nameTag.innerHTML = coderName;

        // display followers
        let followerTag = document.querySelector("#followers");
        let coderFollowers = coderData['followers'] + " followers";
        followerTag.innerHTML = coderFollowers;

        // display avatar
        let avatarTag = document.querySelector("#avatar-img");
        let coderAvatar = coderData["avatar_url"];
        avatarTag.src = coderAvatar;

    })
    .catch(err => console.log(err) );
}

function searchUsername(){
    let username_input = document.querySelector("#username");
    let search_term = username_input.value;
    console.log(search_term)
    fetch(`https://api.github.com/users/${search_term}`)
    .then(response => response.json() )
    .then(coderData => {
        console.log(coderData);
        // display name
        let nameTag = document.querySelector("#name");
        let coderName = coderData['name'];
        nameTag.innerHTML = coderName;
        // display followers
        let followerTag = document.querySelector("#followers");
        let coderFollowers = coderData['followers'] + " followers";
        followerTag.innerHTML = coderFollowers;
        // display avatar
        let avatarTag = document.querySelector("#avatar-img");
        let coderAvatar = coderData["avatar_url"];
        avatarTag.src = coderAvatar;
    })
    .catch(err => console.log(err) );
}