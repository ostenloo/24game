<div> 
    <h1 class = "pt-4 text-center text-2xl font-semibold">
        24 Game
    </h1>
    {#if showPopup}
    <Popup bind:showPopup yes={yes}/>
    {:else}
    <Lobby/> 
    {/if}
</div> 

<style lang="postcss">
  :global(html) {
    background-color: theme(colors.gray.100);
  }
</style>

<script>
	import Popup from '../components/popup.svelte';
  import Lobby from '../components/lobby.svelte';
  let showPopup = true; 
  let yes = false;
</script>