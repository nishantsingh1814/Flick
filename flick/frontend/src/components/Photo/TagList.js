import React from "react";
import Tag from "./Tag";

const TagList = ({tags}) => {

    const tagItems = tags.map((tag, index) => {
        return (
            <Tag
                tag={tag.tag}
                key={index}
            />
        );
    });
    return (
        <div id="tag-list">
            {tagItems}
        </div>
    );
};

export default TagList;
