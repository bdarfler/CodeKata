class KataTwo

  def self.chop_iterative(target, list)
    first = 0
    last = list.size - 1
    while first <= last do
      mid = (first + last) / 2
      if list[mid] < target
        first = mid + 1
      elsif list[mid] > target
        last = mid - 1
      else
        return mid
      end
    end
    return -1
  end

  def self.chop_recursive(target, list)
    return recursive_helper(target, list, 0, list.size - 1)
  end

  def self.recursive_helper(target, list, first, last)
    return -1 if first > last
    mid = first + (last - first) / 2
    if list[mid] < target
      recursive_helper(target, list, mid + 1, last)
    elsif list[mid] > target :
      recursive_helper(target, list, first, mid - 1)
    else
      mid
    end
  end

  def self.slice_recursive(target, list)
    slice_recursive_helper(target, list, 0)
  end

  def self.slice_recursive_helper(target, list, offset)
    return -1 unless list.any?
    mid = list.size / 2
    if list[mid] < target
      slice_recursive_helper(target, list[mid+1, list.size], mid + 1)
    elsif list[mid] > target
      slice_recursive_helper(target, list[0, mid], offset)
    else
      offset + mid
    end
  end

  def self.slice_iterative(target, list)
    offset = 0
    while list.any? do
      mid = list.size / 2
      if list[mid] < target
        offset = mid + 1
        list = list[mid + 1, list.size]
      elsif list[mid] > target
        list = list[0, mid]
      else
        return offset + mid
      end
    end
    return -1
  end

  def self.chop(target, list)
    return -1 unless list.any?
    mid = list.size / 2
    if list[mid] < target
      ret = chop(target, list[mid + 1, list.size])
      ret == -1 ? ret : mid + 1 + ret
    elsif list[mid] > target
      chop(target, list[0, mid])
    else
      mid
    end
  end
end