<script>
  import jQuery from "jquery"
	let result_text = "None"
	const search_bar = '<form id="form" role="search"> <input type="search" id="query" name="q" placeholder="Query", aria-label="Query here"> </form>'
	// role and aria-label are for screen reader accessibility
	/**
	 * Handle click on Search Button, sending POST request with query to Python code, recieving and handling response
	 * @returns {void}
	 */
	function onClick(){
		let user_query = String(document.getElementById('query').value)
		let payload = {
			"query": user_query,
		}
		jQuery.post('//localhost:8000/query', payload, function(data){
			data = JSON.parse(data)
			let function_result = String(data.result)
			result_text = function_result
			//ToDo: Other stuff with response
		}).fail(function(data){
			//ToDo: Add more specific error messages based on errors recieved from backend
			alert("Failed")
		})
	}
</script>

<main>
  <!-- First div handles search bar and button -->
	<div style="display:flex; flex-direction: row; justify-content: center; align-items: center">
		{@html search_bar}
		<button on:click="{onClick}">Search</button>
	</div>
	<!-- Second div is spacing -->
	<div>
		<p class="space"></p>
	</div>
	<!-- Third div has graph image and paper list-->
	<div style="display:flex; flex-direction: row; justify-content: space-between">
		<img src="test-image.jpg" alt="graph size tester" width="1024" height="720">
    <!-- Kind of hacky but it makes the spacing work for the minute. Might rework later -->
    <span style="display:inline-block; width: 2cm;"></span>
		<dl class="dl-horizontal text-muted">
			<dt>Paper one - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper two - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper three - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id<dd>
			<dt>Paper four - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper five (very long title) - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper six - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper seven - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper eight - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper nine - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
			<dt>Paper ten - Authors</dt>
			<dd class="link">https://arxiv.org/abs/id</dd>
		</dl>
	</div>
	<p>{result_text}</p>
</main>

<style>
  main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	.space{
		margin-bottom: 1.2cm;
	}

	.dl-horizontal dt {
		text-align: left; 
	}

	.link {
		font-size: small;
	}
</style>
