<main>
    <h1>Visitor Counter</h1>
    <p>Current Visitor Count:</p>
    <div class="visitor-count">
        {#if loading}
            <div class="spinner"></div> <!-- Rueda giratoria -->
        {:else}
            {visitorCount}
        {/if}
    </div>
    <div class="footer">
        <p>Welcome to our website!</p>
        <p>Stay connected!</p>
    </div>
</main>

<script>
    import { onMount } from 'svelte';
    import socket from '$lib/socket';
  
    let visitorCount = 0;
    let loading = true;

    onMount(() => {
        socket.on('update_visits', (data) => {
            visitorCount = data.visits; 
            loading = false;
        });
        socket.emit('newVisitor');
        return () => {
            socket.off('update_visits');
        };
    });
</script>


<style>
    main {
        text-align: center;
        padding: 2em;
        max-width: 600px;
        margin: 0 auto;
        font-family: 'Arial', sans-serif;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: #333;
        font-size: 2.5em;
        margin-bottom: 0.5em;
    }

    p {
        font-size: 1.5em;
        color: #555;
        margin: 0.5em 0;
    }

    .visitor-count {
        font-size: 3em;
        color: #007bff;
        font-weight: bold;
        margin: 1em 0;
    }

    .spinner {
        border: 8px solid #f3f3f3; /* Color de fondo */
        border-top: 8px solid #3498db; /* Color de la parte superior */
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 1s linear infinite; /* Efecto de giro */
        margin: 0 auto; /* Centra la rueda */
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .footer {
        margin-top: 2em;
        font-size: 0.9em;
        color: #777;
    }
</style>

