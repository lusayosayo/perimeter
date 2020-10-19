@extends('layouts.administration_interface.table_index')

@section('table_content')
	@if(count($users) > 0)
	<div>
		@if($mode == "functional_users")
		<h3>Users</h3>
		@elseif($mode == "pending_approval")
		<h3>Pending Approvals</h3>
		@endif
			<table class="table">
				<thead class="thead-dark">
					<th scope="col">ID</th>
					<th scope="col">User Name</th>
					<th scope="col">Email</th>
					<th scope="col">Account Status</th>
					<th scope="col">User Group</th>
				</thead>
				<tbody>
				@foreach($users as $user)
					<tr class="modifiable_row" onclick="handleUserAction('view', {{ $user -> id }})">
						<th scope="row">{{ $user -> id }}</th>
						<td>{{ $user -> name }}</td>
						<td>{{ $user -> email }}</td>
						<td>{{ $user -> account_status }}</td>
						<td>{{ $user -> user_group_name }}</td>
					</tr>
				@endforeach
				</tbody>
			</table>
		
	</div>
	@else
		<div class="flex-center position-ref full-height">
            <div class="code">
            	@if($mode == "functional_users")
                <h1>No users found --- Impossible  </h1>
               	@elseif($mode == "pending_approval")
               	</h1>No pending users at the moment...</h1>
               	@endif
              
            </div>
            <br>
            <div class="message" style="padding: 10px;">
            	<span class="fa fa-terminal"></span>
            	@if($mode == "functional_users")
                <a href="/users/create">Add a new user</a> to get started.
                @elseif($mode == "pending_approval")
                <span>Maybe it's time for a cup of coffee.</span>
                @endif
            </div>
        </div>
	@endif
@endsection

@section('scripts')
<script>
	function handleUserAction(action, id) {
		switch(action) {
			case 'view': {
				window.location.assign('/users/' + id);
			} break;
		}
	}

</script>
@endsection