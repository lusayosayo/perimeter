@extends("layouts.administration_interface.create_update")

@section('create_update_content')
		<form action="/user_groups" method="POST">
			<h3>Create User Group</h3>
			<div class="form-group row">
				<label for="user_group_name" class="col-sm-3 col-form-label">Group Name: </label>
				<div class="col-sm-9">
					<input type="text" name="user_group_name" class="form-control" required placeholder="Junior IT Officers"/>
				</div>
			</div>
			<div class="form-group row">
				<label for="user_group_description" class="col-sm-3 col-form-label">Description: </label>
				<div class="col-sm-9">
					<textarea class="form-control" name="user_group_description" placeholder="I.T officers interning for the I.T office..."></textarea>
				</div>
			</div>

			<div class="form-group row">
				<div class="col-sm-3">
				</div>
				<div class="col-sm-9">
					<button type="submit" class="btn btn-outline-dark mr-1">Create User Group</button>
				</div>
			</div>
			<input type="hidden" name="_token" value="<?php echo csrf_token(); ?>">
			<input type="hidden" name="_method" value="POST"/>
		</form>
@endsection