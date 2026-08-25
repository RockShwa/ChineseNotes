<script lang="ts">
    import { onMount } from 'svelte';

    // state declares a reactive variable with a non-computed value
    // $derived(a + b) would declare a computed value (sum of a & b)
    let randNum = $state();

    onMount(async () => {
        const response = await fetch('http://localhost:8000/rand');
        const data = await response.json();
        randNum = data.number;
    })
</script>

<main>
   <h1>Welcome to SvelteKit</h1>
    <p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>

    <div>
        {randNum}
    </div> 
</main>


