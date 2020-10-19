@extends('layouts.administration_interface.table_index')

@section('table_content')
	@if(count($user_groups) > 0)
	<div>
		<h3>User Groups</h3>
		<table class="table">
			<thead class="thead-dark">
				<th scope="col">ID</th>
				<th scope="col">User Group Name</th>
				<th scrope="col">User Group Description</th>
			</thead>
			<tbody>
			@foreach($user_groups as $user_group)
				<tr class="modifiable_row" onclick="handleNetworkProviderAction('view', {{ $user_group -> id }})">
					<th scope="row">{{ $user_group -> id }}</th>
					<td>{{ $user_group -> name }}</td>
					<td>{{ $user_group -> description }}</td>
			@endforeach
			</tbody>
		</table>
		
	</div>
	@else
		<div class="flex-center position-ref full-height">
            <div class="code">
                <h1>
                	No User Groups Found
                </h1>
            </div>
            <br>
            <div class="message" style="padding: 10px;">
            	<span class="fa fa-terminal"></span>
                <a href="/user_groups/create">Add a User Group</a> to get started.
            </div>
        </div>
	@endif
@endsection

@section('scripts')
<script>
	function handleNetworkProviderAction(action, id) {
		switch(action) {
			case 'view': {
				window.location.assign('/user_groups/' + id);
			} break;
		}
	}

</script>
@endsection