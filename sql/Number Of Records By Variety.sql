select variety,count(variety) from [dbo].[iris]
group by variety
order by variety asc;