<div class = "border border shadow-md rounded-md h-fit w-[40rem] z-10 inset-1/2 -translate-x-2/4 -translate-y-3/4 absolute"> 
    <div class = "p-[2rem]"> 
        <div class = "gap-4 flex flex-col justify-center items-center"> 
            <div class = "text-2xl font-semibold"> Welcome to 24 Game. </div> 
            <div class = "text-md"> <span class = "font-bold"> 24 Game </span> is a free, real-time web application that allows you to play 
            the game 24 with users over the internet. This site features a chatroom, a lobby, and a global leaderboard. Invite your friends to play with private rooms. 
            Sign up to save your results on the leaderboard. </div> 
            <div class = "text-md"> Currently, we offer 2 game modes: Traditional and Set. You can learn about the rules in the About section. </div> 
            <label>
            <input type=checkbox bind:checked={yes}>
                Don't Show Again
            </label>
            <button class = "text-md w-fit text-green-500 hover:bg-green-200 px-[0.5rem] py-[0.2rem] rounded-md border border-solid border-green-500"
                on:click={handleClick}> 
                Enter 
            </button> 
        </div> 
    </div> 
</div> 

<script>
	export let yes; 
    export let showPopup; 
    function handleClick() {
		showPopup = false;  
	}
</script>