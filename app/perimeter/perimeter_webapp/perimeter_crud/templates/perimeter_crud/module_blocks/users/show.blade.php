@extends("layouts.administration_interface.create_update")

@section('create_update_content')
		<div>
			<div class="form-group row">
				<label for="username" class="col-sm-3 col-form-label">User Name: </label>
				<div class="col-sm-9">
					<input type="text" name="username" class="form-control disabled" disabled placeholder="Victoria Avenue VBS user" value="{{ $user->name }}"/>
				</div>
			</div>
			<div class="form-group row">
				<label for="email" class="col-sm-3 col-form-label">Email: </label>
				<div class="col-sm-9">
					<input type="email" name="email" class="form-control disabled" disabled placeholder="172.25.0.1" value="{{ $user->email }}"/>
				</div>
			</div>

			<div class="form-group row">
				<label for="userDescription" class="col-sm-3 col-form-label">Account Status: </label>
				<div class="col-sm-9">
					<input type="text" name="account_status" value="{{ $account_status -> account_status }}" class="form-control" disabled/>
				</div>
			</div>

			<div class="form-group row">
				<label for="userGroup" class="col-sm-3 col-form-label">User Group: </label>
				<div class="col-sm-9">
					<input type="text" name="user_group" value="{{ $user_group -> name }}" class="form-control" disabled/>
				</div>
			</div>

			<div class="form-group row">
				<div class="col-sm-3">
				</div>
				<div class="col col-sm-9">
					@if($user->account_status == 1 && Auth::user()->account_status == 3)
					<button onclick="approveUser('{{$user->id}}')" id="approveUser" class="btn btn-dark"><span class="fa fa-check"></span>&nbsp;Approve User </button>
					<button onclick="rejectUser('{{$user->id}}')" id="rejectUser" class="btn btn-dark"><span class="fa fa-close"></span>&nbsp;
					 Reject User </button>
					@else
					<a href="/users/{{$user->id}}/edit" id="edit_user" class="btn btn-outline-dark"><span class="fa fa-unlock"></span>&nbsp;
					 Edit User </a>
					 @endif
				</div>
			</div>
			<input type="hidden" name="_token" value="<?php echo csrf_token(); ?>"/>
		</div>
@endsection
@section('scripts')
<script>
	function approveUser(id) {
		location.assign("/users/" + id +"/approve");
	}

	function rejectUser(id) {
		if (confirm("Are you sure you want to reject this user?")) {
			location.assign("/users/" + id +"/reject");
		} else {

		}
	}
</script>
@endsection