@extends("layouts.administration_interface.create_update")

@section('create_update_content')
		<div>
			<h3>View User Group</h3>
			<div class="form-group row">
				<label for="user_group_name" class="col-sm-3 col-form-label">User Group Name: </label>
				<div class="col-sm-9">
					<input type="text" name="name" class="form-control" disabled value="{{$user_group -> name}}"/>
				</div>
			</div>
			<div class="form-group row">
				<label for="user_group_description" class="col-sm-3 col-form-label">User Group Description: </label>
				<div class="col-sm-9">
					<textarea class="form-control" name="description" disabled>{{$user_group-> description}}</textarea>
				</div>
			</div>

			<div class="form-group row">
				<div class="col-sm-3">
				</div>
				<div class="col-sm-9">
					<a href="/user_groups/{{$user_group -> id}}/edit" class="btn btn-outline-dark mr-1"><span class="fa fa-unlock"></span> &nbsp; Edit User Group</a>
				</div>
			</div>
			<input type="hidden" name="_token" value="<?php echo csrf_token(); ?>">
		</div>
@endsection