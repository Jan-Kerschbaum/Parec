<script>
    import jQuery from "jquery"
    import vis from "vis"
	import { onMount } from 'svelte'
	let result_text = "None"
	// role and aria-label are for screen reader accessibility
	//Generate initial graph
	let container
	let nodes_array, nodes, edges_array, edges, network
	onMount(() => {
		// ToDo: Do somthing with the initial graph to show it's a placeholder
		nodes_array = [{ id: 0, label: "Node 0" }, { id: 1, label: "Node 1" }, { id: 2, label: "Node 2" }]
		nodes = new vis.DataSet(nodes_array)
		edges_array = [{ from: 0, to: 1 },{ from: 0, to: 2 }]
    	edges = new vis.DataSet(edges_array)
    	var data = {
      		nodes: nodes,
      		edges: edges,
    	};
    	var options = {}
    	network = new vis.Network(container, data, options)
	})
	/**
	 * Handle click on Search Button, sending POST request with query to Python code, recieving and handling response
	 * @returns {void}
	 */
	function onClick(){
		let user_query = String(document.getElementById('query').value)
		let payload = {
			"query": user_query,
		}
		jQuery.post('api/query', payload, function(data){
			data = JSON.parse(data)
			let function_result = String(data.result)
			result_text = function_result
			// Update graph based on edge list returned from backend
			var graph_response = JSON.parse(data.graph)
			var nodesArray = []
			var edgesArray = []
			var current_node_num = 0
			var found_nodes = []
			var ids = {}
			for(var key in graph_response){
				// Note: If the element we're currently looking at is 0:{"from": "a", "to": "b"}, then key is 0, from_node = "a", to_node = "b"
				if(graph_response.hasOwnProperty(key)){
					var val = graph_response[key]
					var from_node = String(val.from)
					var to_node = String(val.to)
					if(!found_nodes.includes(from_node)){
						found_nodes.push(from_node)
						nodesArray.push({id: current_node_num, label: from_node})
						ids[from_node] = current_node_num
						current_node_num += 1
					}
					if(!found_nodes.includes(to_node)){
						found_nodes.push(to_node)
						nodesArray.push({id: current_node_num, label: to_node})
						ids[to_node] = current_node_num
						current_node_num += 1
					}
					edgesArray.push({from: ids[from_node], to: ids[to_node]})
					nodes.clear()
					edges.clear()
					nodes.add(nodesArray)
					edges.add(edgesArray)
				}
			}
			
		}).fail(function(data){
			//ToDo: Add more specific error messages based on errors recieved from backend
			alert("Failed")
		})
	}
</script>

<main>
  <!-- First div handles search bar and button -->
	<div style="display:flex; flex-direction: row; justify-content: center; align-items: center">
		<form id="form" role="search">
			<input type="search" id="query" name="q" placeholder="Query" aria-label="Query here">
		</form>
		<button on:click={onClick}>Search</button>
	</div>
	<!-- Second div is spacing -->
	<div>
		<p class="space"></p>
	</div>
	<!-- Third div has graph image and paper list-->
	<div style="display:flex; flex-direction: row; justify-content: space-between">
		<div id="graph" bind:this={container}></div>
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

	#graph {
		width: 1024px;
		height: 720px;
		border: 1px solid lightgray;
	}
</style>
