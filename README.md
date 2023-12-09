# godzilla_stroy_point

## requirements
- python
- rye

## usage

### setup

#### 1. Toggl auth

- get toggl token from [here](https://track.toggl.com/profile/) and write it in `secrets/toggl_token.py` like this

```python
toggl_token = "tokentokentokentoken"
```

#### 2. Jira auth

- get jira token from [here](https://id.atlassian.com/manage-profile/security/api-tokens).
- write it in `secrets/jira-token`
- write your Jira email address in `secrets/jira-email`
- run `make jira_token`

## development

now, develop this app in main branch

install by `make install`

develop and format by `make format`

## tips

`make help` available
