teamFixtureQuery = """
query teamFixture($teamID: ID!) {
  discoverTeam(teamID: $teamID) {
    id
    name
    season { id name __typename }
    grade { id name __typename }
    organisation { id name __typename }
    __typename
  }
  discoverTeamFixture(teamID: $teamID) {
    id
    name
    isStale
    provisionalDates
    grade {
      id
      name
      type
      season {
        id
        name
        competition {
          id
          name
          organisation { id name __typename }
          type
          __typename
        }
        __typename
      }
      hideScores
      __typename
    }
    fixture {
      ...RoundFixtureFragment
      __typename
    }
    __typename
  }
}

fragment RoundFixtureFragment on DiscoverRoundFixture {
  byes {
    ...RoundFixtureDiscoverTeamFragment
    __typename
  }
  games {
    id
    alias
    pool { id name __typename }
    away { ...RoundFixtureTeamFragment __typename }
    home { ...RoundFixtureTeamFragment __typename }
    result {
      winner { name value __typename }
      outcome { name value __typename }
      home {
        outcome { name value __typename }
        statistics { count type { value __typename } __typename }
        periods {
          period { label value __typename }
          type
          closureStatus
          statistics { count type { label value __typename } __typename }
          __typename
        }
        gameOutcomeDescription
        __typename
      }
      away {
        outcome { name value __typename }
        statistics { count type { value __typename } __typename }
        periods {
          period { label value __typename }
          type
          closureStatus
          statistics { count type { label value __typename } __typename }
          __typename
        }
        __typename
      }
      __typename
    }
    status { name value __typename }
    date
    dates
    allocation {
      time
      dateTimeList { date time __typename }
      court {
        id
        name
        abbreviatedName
        latitude
        longitude
        venue {
          id name abbreviatedName latitude longitude
          address suburb state postcode country
          __typename
        }
        __typename
      }
      __typename
    }
    isStale
    gameType {
      name
      value
      eScoringSettings {
        dismissalsPerBatter
        legalBallsPerOver
        __typename
      }
      __typename
    }
    __typename
  }
  __typename
}

fragment RoundFixtureDiscoverTeamFragment on DiscoverTeam {
  id
  name
  logo {
    sizes {
      url
      dimensions { width height __typename }
      __typename
    }
    __typename
  }
  season {
    id
    name
    competition { id name __typename }
    __typename
  }
  organisation { id name type __typename }
  __typename
}

fragment RoundFixtureTeamFragment on DiscoverPossibleTeam {
  ... on ProvisionalTeam {
    name
    pool { id name __typename }
    __typename
  }
  ...RoundFixtureDiscoverTeamFragment
  __typename
}
"""