<div> 
    <div class = "flex flex-row items-center p-4 gap-8"> 
      <h1 class = "text-3xl font-semibold">
          24 Game
      </h1>
    </div>
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