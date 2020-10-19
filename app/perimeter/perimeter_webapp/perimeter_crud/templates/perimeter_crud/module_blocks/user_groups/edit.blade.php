@extends("layouts.administration_interface.create_update")

@section('create_update_content')
		<form action="/user_groups/{{ $user_group->id }}" method="POST">
			<h3>View Cluster</h3>
			<div class="form-group row">
				<label for="user_group_name" class="col-sm-3 col-form-label">Group Name: </label>
				<div class="col-sm-9">
					<input type="text" name="user_group_name" class="form-control" required value="{{$user_group-> name}}"/>
				</div>
			</div>
			<div class="form-group row">
				<label for="user_group_description" class="col-sm-3 col-form-label">Description: </label>
				<div class="col-sm-9">
					<textarea class="form-control" name="user_group_description" required>{{$user_group-> description}}</textarea>
				</div>
			</div>

			<div class="form-group row">
				<div class="col-sm-3">
				</div>
				<div class="col-sm-9">
					<button href="/user_groups/{{$user_group-> id}}" class="btn btn-outline-dark mr-1"><span class="fa fa-save"></span> &nbsp; Save Changes</button>
				</div>
			</div>
			<input type="hidden" name="_method" value="PUT"/>
			<input type="hidden" name="_token" value="<?php echo csrf_token(); ?>">
		</form>
@endsection