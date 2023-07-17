create table GITHUB_EVENTS(
	id SERIAL,
	repo_id VARCHAR(255),
	event_type VARCHAR(255),
	event_timestemp timestamp with time zone
);