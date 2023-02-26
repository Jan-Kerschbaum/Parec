<script>
    import jQuery from "jquery"
    import vis from "vis"
	import { onMount } from 'svelte'
	let result_text = "None"
	let PaperOneName = "Paper One"
	let PaperOneAuthors = "Authors"
	let PaperOneID = "id"
	let PaperTwoName = "Paper Two"
	let PaperTwoAuthors = "Author"
	let PaperTwoID = "id"
	let PaperThreeName = "Paper Three"
	let PaperThreeAuthors = "Authors"
	let PaperThreeID = "id"
	let PaperFourName = "Paper Four"
	let PaperFourAuthors = "Authors"
	let PaperFourID = "id"
	let PaperFiveName = "Paper Five"
	let PaperFiveAuthors = "Authors"
	let PaperFiveID = "id"
	let PaperSixName = "Paper Six"
	let PaperSixAuthors = "Authors"
	let PaperSixID = "id"
	let PaperSevenName = "Paper Seven"
	let PaperSevenAuthors = "Authors"
	let PaperSevenID = "id"
	let PaperEightName = "Paper Eight"
	let PaperEightAuthors = "Authors"
	let PaperEightID ="id"
	let PaperNineName = "Paper Nine"
	let PaperNineAuthors = "Authors"
	let PaperNineID = "id"
	let PaperTenName = "Paper Ten"
	let PaperTenAuthors = "Authors"
	let PaperTenID = "id"
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
    	var options = {
			groups:{
				"queryGroup": {
					color:{
						background:'#4f0d02',
						border: "#6e180a"
					},
					font:{
						multi: true,
						color: "#ffffff"
					},
				"shape": "box",
				}
			}
		}
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
		jQuery.post('//localhost:8000/query', payload, function(data){
			data = JSON.parse(data)
			let function_result = String(data.result)
			result_text = function_result
			//Update paper list based on return from backend
			var paper_response = JSON.parse(data.papers)
			//TODO: This, as well as the define structure that required it above needs to be refactored
			PaperOneName = String(paper_response[0].name)
			PaperOneAuthors = String(paper_response[0].authors)
			PaperOneID = String(paper_response[0].id)
			PaperTwoName = String(paper_response[1].name)
			PaperTwoAuthors = String(paper_response[1].authors)
			PaperTwoID = String(paper_response[1].id)
			PaperThreeName = String(paper_response[2].name)
			PaperThreeAuthors = String(paper_response[2].authors)
			PaperThreeID = String(paper_response[2].id)
			PaperFourName = String(paper_response[3].name)
			PaperFourAuthors = String(paper_response[3].authors)
			PaperFourID = String(paper_response[3].id)
			PaperFiveName = String(paper_response[4].name)
			PaperFiveAuthors = String(paper_response[4].authors)
			PaperFiveID = String(paper_response[4].id)
			PaperSixName = String(paper_response[5].name)
			PaperSixAuthors = String(paper_response[5].authors)
			PaperSixID = String(paper_response[5].id)
			PaperSevenName = String(paper_response[6].name)
			PaperSevenAuthors = String(paper_response[6].authors)
			PaperSevenID = String(paper_response[6].id)
			PaperEightName = String(paper_response[7].name)
			PaperEightAuthors = String(paper_response[7].authors)
			PaperEightID = String(paper_response[7].id)
			PaperNineName = String(paper_response[8].name)
			PaperNineAuthors = String(paper_response[8].authors)
			PaperNineID = String(paper_response[8].id)
			PaperTenName = String(paper_response[9].name)
			PaperTenAuthors = String(paper_response[9].authors)
			PaperTenID = String(paper_response[9].id)
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
						if(from_node == user_query){
							nodesArray.push({id: current_node_num, group: "queryGroup", label: "<b>" + from_node + "</b>"})
						}else{
							nodesArray.push({id: current_node_num, label: from_node})
						}
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
			//Should only fail from API implementation on a 422 code (unprocessable entity)
			result_text = "Empty Query Field"
			nodes.clear()
			edges.clear()
			//ToDo: Set List Bindings to empty strings
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
			<dt>{PaperOneName}</dt>
			<dd class="authors">{PaperOneAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperOneID}">Link</a>
			</dd>
			<dt>{PaperTwoName}</dt>
			<dd class="authors">{PaperTwoAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperTwoID}">Link</a>
			</dd>
			<dt>{PaperThreeName}</dt>
			<dd class="authors">{PaperThreeAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperThreeID}">Link</a>
			</dd>
			<dt>{PaperFourName}</dt>
			<dd class="authors">{PaperFourAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperFourID}">Link</a>
			</dd>
			<dt>{PaperFiveName}</dt>
			<dd class="authors">{PaperFiveAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperFiveID}">Link</a>
			</dd>
			<dt>{PaperSixName}</dt>
			<dd class="authors">{PaperSixAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperSixID}">Link</a>
			</dd>
			<dt>{PaperSevenName}</dt>
			<dd class="authors">{PaperSevenAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperSevenID}">Link</a>
			</dd>
			<dt>{PaperEightName}</dt>
			<dd class="authors">{PaperEightAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperEightID}">Link</a>
			</dd>
			<dt>{PaperNineName}</dt>
			<dd class="authors">{PaperNineAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperNineID}">Link</a>
			</dd>
			<dt>{PaperTenName}</dt>
			<dd class="authors">{PaperTenAuthors}</dd>
			<dd class="link">
				<a href="https://arxiv.org/abs/{PaperTenID}">Link</a>
			</dd>
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
		text-align: left;
	}

	.authors{
		text-align: left;
		font-size: small;
	}

	#graph {
		width: 1024px;
		height: 720px;
		border: 1px solid lightgray;
	}
</style>
