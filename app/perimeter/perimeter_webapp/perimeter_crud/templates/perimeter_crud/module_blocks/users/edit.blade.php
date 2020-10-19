@extends("layouts.administration_interface.create_update")

@section('create_update_content')
		<form action="/users/{{ $user -> id }}" method="POST">
			<div class="form-group row">
				<label for="username" class="col-sm-3 col-form-label">User Name: </label>
				<div class="col-sm-9">
					<input type="text" name="username" class="form-control required" required placeholder="Victoria Avenue VBS user" value="{{ $user->name }}"/>
				</div>
			</div>
			<div class="form-group row">
				<label for="email" class="col-sm-3 col-form-label">Email: </label>
				<div class="col-sm-9">
					<input type="email" name="email" class="form-control" disabled placeholder="172.25.0.1" value="{{ $user->email }}"/>
				</div>
			</div>

			<div class="form-group row">
				<label for="userDescription" class="col-sm-3 col-form-label">Account Status: </label>
				<div class="col-sm-9">
					<input type="text" id="account_status" disabled value="{{ $account_status -> account_status }}" class="form-control"/>
				</div>
				<div class="col-sm-3">
				</div>
				<div class="col-sm-9 offset-left-3 mt-2">
					<select onchange='updateValueWatcher(this)' class="form-control custom-select custom-control-inline " for="account_status" name="account_status" id="account_status_select">
						@foreach($account_statuses as $account_status) 
							<option value="{{$account_status->id}}">{{$account_status->account_status}}</option>
						@endforeach
					</select>
				</div>
			</div>

			<div class="form-group row">
				<label for="userGroup" class="col-sm-3 col-form-label">User Group: </label>
				<div class="col-sm-9">
					<input type="text" id="user_group" disabled value="{{ $user_group -> name }}" class="form-control"/>
				</div>
				<div class="col-sm-3">
				</div>
				<div class="col-sm-9 offset-left-3 mt-2">
					<select onchange="updateValueWatcher(this)" class="form-control custom-select custom-control-inline " for="user_group" name="user_group">
						@foreach($user_groups as $user_group) 
							<option value="{{$user_group->id}}">{{$user_group->name}}</option>
						@endforeach
					</select>
				</div>
			</div>

			<div class="form-group row">
				<div class="col-sm-3">
				</div>
				<div class="col col-sm-9">
					@if($user->account_status == null && Auth::user()->account_status == 31337)
					<button onclick="approveUser('{{$user->id}}')" id="approveUser" class="btn btn-dark"><span class="fa fa-check"></span>&nbsp;Approve User </button>
					<button onclick="rejectUser('{{$user->id}}')" id="rejectUser" class="btn btn-dark"><span class="fa fa-close"></span>&nbsp;
					 Reject User </button>
					@else
					<button type="submit" class="btn btn-outline-dark"><span class="fa fa-save"></span> &nbsp;Save Changes</button>
					 @endif
				</div>
			</div>
			<input type="hidden" name="_method" value="PUT"/>
			<input type="hidden" name="_token" value="<?php echo csrf_token(); ?>"/>
		</form>
@endsection
@section('scripts')
<script>
	document.getElementById('account_status_select').value="{{$account_status -> account_status}}"
	function approveUser(id) {
		location.assign("/users/" + id +"/approve");
	}

	function rejectUser(id) {
		if (confirm("Are you sure you want to reject this user?")) {
			location.assign("/users/" + id +"/reject");
		} else {

		}
	}

	function updateValueWatcher(input) {
		var watcher = document.getElementById(input.name);
		watcher.value = input.value;
	}
</script>
@endsection