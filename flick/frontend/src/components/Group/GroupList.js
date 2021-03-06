import React from "react";
import GroupCard from "./GroupCard";


const GroupList = ({data}) => {
    const groupItems = data.results.map((group, index) => {
        return (
            <GroupCard
                group={group}
                key={index}
            />
        );
    });
    return (
        <div id="group-container">
            {groupItems}
        </div>
    );
};

export default GroupList;
