import {TaskFilters, getFilterQuery} from "./task";
import {search} from "./search";

export interface Monitor {
    charts(
        app_name: string,
        app_env: string | undefined,
        order: string | "desc",
        filters: TaskFilters,
    ): any;
}

export class MonitorSearch implements Monitor {
    charts(
        app_name: string,
        app_env: string | undefined,
        order: string | "desc",
        filters: TaskFilters,
    ) {
        return search(
            app_name,
            {
                query: {
                    "bool": {
                        "must": getFilterQuery(app_env, filters)
                    }
                },
                sort: [
                    {"timestamp": {"order": order}},
                ],
                aggs: {
                    tasksDistribution: {
                        "terms": {"field": "name", "size": 1000},
                        aggs: {
                            statesDistribution: {
                                "terms": {"field": "state", "size": 1000}
                            },
                            runtimeDistribution: {"avg": {"field": "runtime"}}
                        }
                    },
                    statesDistribution: {
                        "terms": {"field": "state", "size": 1000}
                    },
                    routingKeysDistribution: {
                        "terms": {"field": "routing_key", "size": 1000}
                    },
                    timeDistribution: {
                        "date_histogram": {
                            "field": "timestamp",
                            "calendar_interval": "1m",
                        }
                    },
                }
            },
            {
                size: 0,
                from_: 0
            }
        )
    }
}